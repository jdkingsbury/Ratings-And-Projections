import TableComponent from "~/components/utils/table";
import { PlayerGameLog } from "./types";
import { omitKeys } from "~/components/utils/omitKeys";

export default function RecentGames({ games }: { games: PlayerGameLog[] }) {
  const keysToOmit: (keyof PlayerGameLog)[] = [
    "SEASON_ID",
    "PERSON_ID",
    "GAME_ID",
    "OREB",
    "DREB",
    "VIDEO_AVAILABLE",
    "PLUS_MINUS",
  ];

  const filteredGameLogColumns = games.map((obj) => omitKeys(obj, keysToOmit));

  return (
    <div className="container mx-auto py-2 px-4 sm:px-6">
      <div className="overflow-x-auto">
        <TableComponent
          data={filteredGameLogColumns}
          className="min-w-full divide-y divide-gray-200"
          caption="Recent Games"
        />
      </div>
    </div>
  );
}
