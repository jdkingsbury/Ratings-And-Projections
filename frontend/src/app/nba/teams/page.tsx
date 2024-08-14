import { Card } from "@/components/ui/card";
import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import axios from "axios";
import { Team, Division } from "./types";
import DivisionTeamLists from "./divisions";

type FetchTeamData = {
  data: Division[] | null;
  error: string | null;
};

async function fetchTeams(): Promise<FetchTeamData> {
  try {
    const response = await axios.get<Team[]>(
      `${BACKEND_API_BASE_URL}/nba/teams`,
    );
    const teams: Team[] = response.data;

    // Maps teams to their division
    const divisionMap: { [key: string]: Team[] } = {};
    teams.forEach((team) => {
      if (!divisionMap[team.division]) {
        divisionMap[team.division] = [];
      }

      divisionMap[team.division].push(team);
    });

    // Converts the map to an array with the team mapped to their division
    const divisionArray: Division[] = Object.entries(divisionMap).map(
      ([divisionName, teams]) => ({
        divisionName,
        teams,
      }),
    );

    return { error: null, data: divisionArray };
  } catch (error: any) {
    console.error(`Failed to fetch teams: ${error.message}`);
    return { error: error.message, data: null };
  }
}

// division holds an array of all the division names and the teams in that division
export default async function TeamsPage() {
  const { data: divisions, error } = await fetchTeams();

  return (
    <div className="w-full p-4">
      <Card className="gap-6 shadow-sm rounded-lg">
        <div className="container mx-auto flex flex-col">
          <div>
            <h2 className="text-2xl font-bold tracking-tighter sm:text-2xl md:text-4xl">
              Teams Page
            </h2>
          </div>
          {error ? (
            <p>Error when fetching teams: {error}</p>
          ) : !divisions ? (
            <p>Teams not found.</p>
          ) : (
            <DivisionTeamLists divisions={divisions} />
          )}
        </div>
      </Card>
    </div>
  );
}
