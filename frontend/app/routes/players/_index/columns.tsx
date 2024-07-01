import { ColumnDef } from "@tanstack/react-table";
import { Player } from "./types";
import { NavLink } from "@remix-run/react";
import { Button } from "~/components/ui/button";
import { ArrowUpDown } from "lucide-react";

export const columns: ColumnDef<Player>[] = [
  {
    header: ({ column }) => {
      return (
        <Button
          variant="ghost"
          onClick={() => {
            column.toggleSorting(column.getIsSorted() === "asc");
          }}
        >
          Player
          <ArrowUpDown className="ml-2 h-4 w-4" />
        </Button>
      );
    },
    accessorKey: "full_name",
    cell: ({ row }) => {
      const players = row.original;

      return (
        <NavLink to={`/players/${players.id}`} className="text-blue-500">
          {players.full_name}
        </NavLink>
      );
    },
  },
];
