
import argparse
import sys
from engine import load_hubs, load_parcels, load_riders, load_pickups, assign_parcels, express_then_normal, heavy_first, RiderLoadIterator
from models import Parcel

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hubs', required=True)
    parser.add_argument('--parcels', required=True)
    parser.add_argument('--riders', required=True)
    parser.add_argument('--pickups')
    parser.add_argument('--assign', action='store_true')
    parser.add_argument('--threshold', type=float, default=2.0)
    parser.add_argument('--preview', action='store_true')
    parser.add_argument('--rider')
    args = parser.parse_args()

    hubs = load_hubs(args.hubs)
    parcels = load_parcels(args.parcels)
    riders = load_riders(args.riders)
    pickups = load_pickups(args.pickups, hubs)

    if args.assign:
        assignments, unassigned = assign_parcels(hubs, riders, parcels, pickups)
        for rider_id, rider_parcels in sorted(assignments.items()):
            total_load = sum(p.weight_kg for p in rider_parcels)
            num_parcels = len(rider_parcels)
            destinations = [p.destination for p in rider_parcels[:3]]
            print(f"{rider_id} | {total_load:.2f} | {num_parcels} | {', '.join(destinations)}")
        print("Unassigned:", sorted(unassigned))

    if args.preview:
        target_riders = [args.rider] if args.rider else [r.rider_id for r in riders.all()]
        for rider_id in target_riders:
            rider_parcels = assignments.get(rider_id, [])
            pipeline = heavy_first(args.threshold)(express_then_normal(iter(rider_parcels)))
            print(f"Preview for {rider_id}:")
            for p in pipeline:
                print(f"  {p.parcel_id} ({p.weight_kg}kg)")

if __name__ == '__main__':
    main()