import csv  # For reading CSV files, like spreadsheets
import logging  # For writing notes about what happens, like a diary
from collections import defaultdict  # A smart list that groups things
from typing import Dict, List, Set, Iterator, Generator, Tuple, Optional  # Helps with types
from models import Hub, Parcel, Rider, PickupPoint, CampusKiosk, DormLocker, OfficeDesk  # Import our blueprints

logger = logging.getLogger(__name__)  # Sets up the diary

# Errors: Like saying "Oops, wrong format!" or "Rule broken!"
class DataFormatError(Exception):
    """Raised for malformed data. Like a broken file."""
    pass

class DomainRuleError(Exception):
    """Raised for domain rule violations. Like trying to carry too much."""
    pass

# Repositories: Like boxes to store hubs, parcels, riders. Easy to find by ID.
class HubRepo:
    """In-memory repository for hubs. A box for all hubs."""
    def __init__(self):
        self._data: Dict[str, Hub] = {}  # Dictionary: ID -> Hub

    def add(self, obj: Hub):
        self._data[obj.get_id()] = obj

    def get(self, id: str) -> Optional[Hub]:
        return self._data.get(id)

    def all(self) -> List[Hub]:
        return list(self._data.values())

    def exists(self, id: str) -> bool:
        return id in self._data

    def ids(self) -> Set[str]:
        return set(self._data.keys())

# Same for parcels and riders – just copy-paste the pattern!
class ParcelRepo:
    """Box for parcels."""
    def __init__(self):
        self._data: Dict[str, Parcel] = {}

    def add(self, obj: Parcel):
        self._data[obj.get_id()] = obj

    def get(self, id: str) -> Optional[Parcel]:
        return self._data.get(id)

    def all(self) -> List[Parcel]:
        return list(self._data.values())

    def exists(self, id: str) -> bool:
        return id in self._data

    def ids(self) -> Set[str]:
        return set(self._data.keys())

class RiderRepo:
    """Box for riders."""
    def __init__(self):
        self._data: Dict[str, Rider] = {}

    def add(self, obj: Rider):
        self._data[obj.get_id()] = obj

    def get(self, id: str) -> Optional[Rider]:
        return self._data.get(id)

    def all(self) -> List[Rider]:
        return list(self._data.values())

    def exists(self, id: str) -> bool:
        return id in self._data

    def ids(self) -> Set[str]:
        return set(self._data.keys())

# Load functions: Read from CSV files, like importing a list.
def load_hubs(path: str) -> HubRepo:
    """Load hubs from CSV. Like reading a list of stores."""
    repo = HubRepo()
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                if len(row) != 3:
                    logger.warning(f"Bad row: {row}")  # Note it and skip
                    continue
                hub_id, hub_name, campus = row
                repo.add(Hub(hub_id, hub_name, campus))
    except Exception as e:
        logger.error(f"Oops loading hubs: {e}")
    return repo

# Same for parcels and riders – they check for bad data and skip.
def load_parcels(path: str) -> ParcelRepo:
    """Load parcels from CSV."""
    repo = ParcelRepo()
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) != 6:
                    logger.warning(f"Bad row: {row}")
                    continue
                parcel_id, recipient, priority, hub_id, destination, weight_kg = row
                try:
                    weight_kg = float(weight_kg)  # Make sure it's a number
                    repo.add(Parcel(parcel_id, recipient, priority, hub_id, destination, weight_kg))
                except ValueError:
                    logger.warning(f"Bad weight: {row}")
    except Exception as e:
        logger.error(f"Oops loading parcels: {e}")
    return repo

def load_riders(path: str) -> RiderRepo:
    """Load riders from CSV."""
    repo = RiderRepo()
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if len(row) != 4:
                    logger.warning(f"Bad row: {row}")
                    continue
                rider_id, name, max_load_kg, home_hub_id = row
                try:
                    max_load_kg = float(max_load_kg)
                    repo.add(Rider(rider_id, name, max_load_kg, home_hub_id))
                except ValueError:
                    logger.warning(f"Bad load: {row}")
    except Exception as e:
        logger.error(f"Oops loading riders: {e}")
    return repo

def load_pickups(path: Optional[str], hubs: HubRepo) -> Dict[str, PickupPoint]:
    """Load pickups or use defaults. Like setting up special spots."""
    pickups = {}
    if path:
        try:
            with open(path, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if len(row) != 4:
                        logger.warning(f"Bad row: {row}")
                        continue
                    pickup_id, label, hub_id, bias = row
                    try:
                        bias = int(bias)
                        pickups[pickup_id] = PickupPoint(pickup_id, hub_id, label, bias)
                    except ValueError:
                        logger.warning(f"Bad bias: {row}")
        except FileNotFoundError:
            logger.warning("No pickups file, using defaults.")
    if not pickups:
        # Defaults for UCU hostels
        hostel_hubs = [h for h in hubs.all() if h.campus == 'UCU']
        for i, hub in enumerate(hostel_hubs[:3]):
            pickups[f'K{i+1}'] = CampusKiosk(f'K{i+1}', hub.hub_id, f'Kiosk at {hub.hub_name}')
            pickups[f'L{i+1}'] = DormLocker(f'L{i+1}', hub.hub_id, f'Locker at {hub.hub_name}')
            pickups[f'D{i+1}'] = OfficeDesk(f'D{i+1}', hub.hub_id, f'Desk at {hub.hub_name}')
    return pickups

# The big function: Assign parcels to riders, like giving jobs.
def assign_parcels(hubs: HubRepo, riders: RiderRepo, parcels: ParcelRepo, pickups: Dict[str, PickupPoint]) -> Tuple[Dict[str, List[Parcel]], Set[str]]:
    """Assign parcels to riders. Rules: Riders only from their hub, don't overload, EXPRESS first."""
    riders_by_hub = defaultdict(list)  # Group riders by hub
    for rider in riders.all():
        riders_by_hub[rider.home_hub_id].append(rider)
    for hub in riders_by_hub:
        riders_by_hub[hub].sort(key=lambda r: r.rider_id)  # Sort by ID

    parcels_by_hub = defaultdict(lambda: {'EXPRESS': [], 'NORMAL': []})  # Group parcels
    for parcel in parcels.all():
        parcels_by_hub[parcel.hub_id][parcel.priority].append(parcel)

    assignments = defaultdict(list)  # Who gets what
    unassigned = set()  # Parcels that couldn't be delivered

    for hub_id, hub_riders in riders_by_hub.items():
        if not hub_riders:
            continue
        rider_index = 0
        for priority in ['EXPRESS', 'NORMAL']:
            hub_parcels = parcels_by_hub[hub_id][priority]
            # Sort by pickup bias for same priority
            def sort_key(p):
                bias = 0
                if 'PICKUP:' in p.destination:
                    pickup_id = p.destination.split('PICKUP:')[1]
                    if pickup_id in pickups:
                        bias = pickups[pickup_id].base_priority_bias
                    else:
                        logger.warning(f"Unknown pickup {pickup_id}")
                return (-bias, p.parcel_id)  # Higher bias first
            hub_parcels.sort(key=sort_key)

            for parcel in hub_parcels:
                assigned = False
                for _ in range(len(hub_riders)):
                    rider = hub_riders[rider_index]
                    current_load = sum(p.weight_kg for p in assignments[rider.rider_id])
                    if current_load + parcel.weight_kg <= rider.max_load_kg:
                        assignments[rider.rider_id].append(parcel)
                        assigned = True
                        break
                    rider_index = (rider_index + 1) % len(hub_riders)
                if not assigned:
                    unassigned.add(parcel.parcel_id)
                rider_index = (rider_index + 1) % len(hub_riders)

    return dict(assignments), unassigned

# Iterator: Like a list you can walk through one by one.
class RiderLoadIterator:
    """Iterator for rider's parcel loads. Shows each parcel and total weight so far."""
    def __init__(self, rider: Rider, parcels: List[Parcel]):
        self.parcels = parcels
        self.index = 0
        self.cumulative = 0.0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.parcels):
            raise StopIteration
        parcel = self.parcels[self.index]
        self.cumulative += parcel.weight_kg
        result = (parcel.parcel_id, parcel.weight_kg, self.cumulative)
        self.index += 1
        return result

# Generators: Like magic pipes that sort parcels.
def express_then_normal(parcels_iter: Iterator[Parcel]) -> Generator[Parcel, None, None]:
    """Generator: EXPRESS first, then NORMAL."""
    express = []
    normal = []
    for p in parcels_iter:
        if p.priority == 'EXPRESS':
            express.append(p)
        else:
            normal.append(p)
    yield from express  # "Yield" means give one at a time
    yield from normal

def heavy_first(threshold_kg: float):
    """Closure for heavy first generator. Heavy parcels (>= threshold) first, then light."""
    def generator(parcels_iter: Iterator[Parcel]) -> Generator[Parcel, None, None]:
        heavy = []
        light = []
        for p in parcels_iter:
            if p.weight_kg >= threshold_kg:
                heavy.append(p)
            else:
                light.append(p)
        yield from heavy
        yield from light
    return generator