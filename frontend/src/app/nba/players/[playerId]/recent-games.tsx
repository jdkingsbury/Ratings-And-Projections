import { TableComponent } from "@/components/utils/table";
import { PlayerGameLog } from "./types";
import { omitKeys } from "@/components/utils/omit-keys";

const columns = [
  { header: "Date", accessorKey: "game_date" },
  { header: "Matchup", accessorKey: "matchup" },
  { header: "Result", accessorKey: "wl" },
  { header: "Min", accessorKey: "min" },
  { header: "FGM", accessorKey: "fgm" },
  { header: "FGA", accessorKey: "fga" },
  { header: "FG%", accessorKey: "fg_pct" },
  { header: "3PM", accessorKey: "fg3m" },
  { header: "3PA", accessorKey: "fg3a" },
  { header: "3P%", accessorKey: "fg3_pct" },
  { header: "FTM", accessorKey: "ftm" },
  { header: "FTA", accessorKey: "fta" },
  { header: "FT%", accessorKey: "ft_pct" },
  { header: "REB", accessorKey: "reb" },
  { header: "AST", accessorKey: "ast" },
  { header: "STL", accessorKey: "stl" },
  { header: "BLK", accessorKey: "blk" },
  { header: "TOV", accessorKey: "tov" },
  { header: "PF", accessorKey: "pf" },
  { header: "PTS", accessorKey: "pts" },
];

export function RecentGames({ data }: { data: PlayerGameLog[] }) {
  const keysToOmit: (keyof PlayerGameLog)[] = [
    "id",
    "season_id",
    "player_id",
    "game_id",
    "oreb",
    "dreb",
    "video_available",
    "plus_minus",
    "season_year",
  ];

  const cleanedData = data.map((item) => omitKeys(item, keysToOmit));

  return (
    <div className="container mx-auto py-8 px-4 md:px-8">
      <div className="shadow rounded-lg p-4 md:p-6">
        <TableComponent
          columns={columns}
          data={cleanedData}
          caption="Recent Games"
        />
      </div>
    </div>
  );
}
