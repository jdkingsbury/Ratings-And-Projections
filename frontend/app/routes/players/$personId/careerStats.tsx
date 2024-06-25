import TableComponent from "~/components/utils/table";
import { CareerStats } from "./types";
import { omitKeys } from "~/components/utils/omitKeys";

export default function PlayerCareerStats({
  player,
}: {
  player: CareerStats[];
}) {
  const keysToOmit: (keyof CareerStats)[] = [
    "PERSON_ID",
    "SEASON_ID",
    "LEAGUE_ID",
    "TEAM_ID",
    "TEAM_ABBREVIATION",
    "PLAYER_AGE",
  ];

  const filteredCareerStatColumns = player.map((obj) => omitKeys(obj, keysToOmit));

  return (
    <div className="container mx-auto py-10 px-4 sm:px-6">
      <h1 className="font-bold mb-4">Player Career Stats</h1>
      <div className="overflow-x-auto">
        <TableComponent
          data={filteredCareerStatColumns}
          className="min-w-full divide-y divide-gray-200"
        />
      </div>
    </div>
  );
}
