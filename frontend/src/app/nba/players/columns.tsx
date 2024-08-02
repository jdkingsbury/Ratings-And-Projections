"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ArrowUpDown } from "lucide-react";
import { ColumnDef } from "@tanstack/react-table";
import { Player } from "./types";
import Image from "next/image";

export const columns: ColumnDef<Player>[] = [
  // Player Column
  {
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
    accessorKey: "full_name",
    cell: ({ row }) => {
      const players = row.original;

      return (
        <div>
          {/* <Image */}
          {/*   src={players.image_url} */}
          {/*   alt={players.first_last} */}
          {/*   quality={100} */}
          {/*   width={40} */}
          {/*   height={40} */}
          {/*   className="rounded-md object-cover mr-6" */}
          {/* /> */}

          <Link href={`/nba/players/${players.player_id}`}>
            {players.first_last}
          </Link>
        </div>
      );
    },
  },
  // Team
  // Number
  // Position
  // Height
  // Weight
  // School
  // Country
];
