"use client";

import { buttonVariants } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Division } from "./types";
import Link from "next/link";

type DivisionListProps = {
  divisions: Division[];
};

// Component display all the divisions and the teams in them and creates links to navigate to the team page
function DivisionTeamLists({ divisions }: DivisionListProps) {
  return (
    <div className="grid grid-cols-2 gap-6">
      {divisions.map((division, index) => (
        <Card key={index} className="p-4 rounded-md">
          <h2 className="text-xl font-semibold">{division.divisionName}</h2>
          <ul>
            {division.teams.map((team) => (
              <li key={team.team_id} className="p-4">
                <Link
                  href={`/nba/teams/${team.team_id}`}
                  className={buttonVariants({ variant: "ghost" })}
                >
                  {team.name}
                </Link>
              </li>
            ))}
          </ul>
        </Card>
      ))}
    </div>
  );
}

export default DivisionTeamLists;
