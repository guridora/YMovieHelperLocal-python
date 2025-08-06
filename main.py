import argparse
from scenario_parser import ScenarioParser

def main():
    parser = argparse.ArgumentParser(description="YMovieHelperLocal - Scenario Parser CLI")
    parser.add_argument("scenario_file", help="Path to the scenario file (e.g., scenario.txt)")
    args = parser.parse_args()

    scenario_parser = ScenarioParser(args.scenario_file)
    scenario_data = scenario_parser.parse()

    print("Parsed Scenario:")
    for scene in scenario_data:
        print(scene)

if __name__ == "__main__":
    main()
