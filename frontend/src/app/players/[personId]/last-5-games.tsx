import { TableComponent } from "@/components/utils/table";
import { PlayerGameLog } from "./types";
import { omitKeys } from "@/components/utils/omit-keys";

const columns = [
  { header: "Date", accessorKey: "GAME_DATE" },
  { header: "Matchup", accessorKey: "MATCHUP" },
  { header: "Result", accessorKey: "WL" },
  { header: "Min", accessorKey: "MIN" },
  { header: "FGM", accessorKey: "FGM" },
  { header: "FGA", accessorKey: "FGA" },
  { header: "FG%", accessorKey: "FG_PCT" },
  { header: "3PM", accessorKey: "FG3M" },
  { header: "3PA", accessorKey: "FG3A" },
  { header: "3P%", accessorKey: "FG3_PCT" },
  { header: "FTM", accessorKey: "FTM" },
  { header: "FTA", accessorKey: "FTA" },
  { header: "FT%", accessorKey: "FT_PCT" },
  { header: "REB", accessorKey: "REB" },
  { header: "AST", accessorKey: "AST" },
  { header: "STL", accessorKey: "STL" },
  { header: "BLK", accessorKey: "BLK" },
  { header: "TOV", accessorKey: "TOV" },
  { header: "PF", accessorKey: "PF" },
  { header: "PTS", accessorKey: "PTS" },
];

export function PlayerLast5Games({ data }: { data: PlayerGameLog[] }) {
  const keysToOmit: (keyof PlayerGameLog)[] = [
    "SEASON_ID",
    "PERSON_ID",
    "GAME_ID",
    "OREB",
    "DREB",
    "VIDEO_AVAILABLE",
    "PLUS_MINUS",
  ];

  const cleanedData = data.map((item) => omitKeys(item, keysToOmit));

  return (
    <div className="container mx-auto py-8 px-4 md:px-8">
      <div className="shadow rounded-lg p-4 md:p-6">
        <TableComponent columns={columns} data={data} caption="Recent Games" />
      </div>
    </div>
  );
}
