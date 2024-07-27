"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowUpDown } from "lucide-react";
import { ColumnDef } from "@tanstack/react-table";
import { Player } from "./types";

export const columns: ColumnDef<Player>[] = [
  // Player Column
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

      return <Link href={`/players/${players.player_id}`}>{players.first_last}</Link>;
    },
  },
];
