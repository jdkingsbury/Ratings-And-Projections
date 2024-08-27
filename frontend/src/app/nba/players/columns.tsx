"use client";

import Image from "next/image";
import { ColumnDef } from "@tanstack/react-table";
import { Player } from "./types";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowUpDown } from "lucide-react";
import BasketballIcon from "@/components/icons/basketball";

// Starting Layout for the players page. This page will probably change when I find the layout I want.

export const columns: ColumnDef<Player>[] = [
  // Displays Player Image
  {
    header: "",
    accessorKey: "id",
    cell: ({ row }) => {
      const players = row.original;

      return (
        <div className="justify-normal">
          <Link href={`/nba/players/${players.player_id}`}>
            <BasketballIcon color="text-primary" />
          </Link>
        </div>
      );
    },
  },
  // Displays the Players Name
  {
    // Code for sorting players in the table when the user clicks the up and down arrow buttons
    header: ({ column }) => {
      return (
        <div>
          <Button
            variant="ghost"
            onClick={() => {
              column.toggleSorting(column.getIsSorted() === "asc");
            }}
          >
            Player
            <ArrowUpDown className="ml-2 h-4 w-4" />
          </Button>
        </div>
      );
    },

    accessorKey: "first_last",

    // Creates the links to navigate to the players profile page
    cell: ({ row }) => {
      const players = row.original;

      return (
        <div className="justify-normal">
          <Link href={`/nba/players/${players.player_id}`}>
            {players.first_last}
          </Link>
        </div>
      );
    },
  },
  {
    // Displays Players Team
    header: "Team",
    accessorKey: "team_name",
  },
  // Displays Players Jersey Number
  {
    header: "Number",
    accessorKey: "jersey",
  },
  // Displays Players Position
  {
    header: "Position",
    accessorKey: "position",
  },
  // Displays School Player Last Attended
  {
    header: "School",
    accessorKey: "school",
  },
  // Displays the Country the Player is from
  {
    header: "Country",
    accessorKey: "country",
  },
];
