import { TableComponent } from "@/components/utils/table";
import { CareerStats } from "./types.ts";
import { omitKeys } from "@/components/utils/omit-keys";

const columns = [
  { header: "GP", accessorKey: "GP" },
  { header: "GS", accessorKey: "GS" },
  { header: "MIN", accessorKey: "MIN" },
  { header: "FGM", accessorKey: "FGM" },
  { header: "FGA", accessorKey: "FGA" },
  { header: "FG%", accessorKey: "FG_PCT" },
  { header: "3PM", accessorKey: "FG3M" },
  { header: "3PA", accessorKey: "FG3A" },
  { header: "3P%", accessorKey: "FG3_PCT" },
  { header: "FTM", accessorKey: "FTM" },
  { header: "FTA", accessorKey: "FTA" },
  { header: "FT%", accessorKey: "FT_PCT" },
  { header: "OREB", accessorKey: "OREB" },
  { header: "DREB", accessorKey: "DREB" },
  { header: "REB", accessorKey: "REB" },
  { header: "AST", accessorKey: "AST" },
  { header: "STL", accessorKey: "STL" },
  { header: "BLK", accessorKey: "BLK" },
  { header: "TOV", accessorKey: "TOV" },
  { header: "PF", accessorKey: "PF" },
  { header: "PTS", accessorKey: "PTS" },
];

export function PlayerCareerStats({ data }: { data: CareerStats[] }) {
  const keysToOmit: (keyof CareerStats)[] = [
    "PERSON_ID",
    "SEASON_ID",
    "LEAGUE_ID",
    "TEAM_ID",
    "TEAM_ABBREVIATION",
    "PLAYER_AGE",
  ];

  const cleanedData = data.map((item) => omitKeys(item, keysToOmit));

  return (
    <div className="container mx-auto py-8 px-4 md:px-8">
      <div className="shadow rounded-lg p-4 md:p-6">
        <h2 className="text-2xl font-semibold mb-4">Stats</h2>
        <TableComponent columns={columns} data={data} caption="Career Stats" />
      </div>
    </div>
  );
}
