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

export default async function TeamsPage() {
  const { data: divisions, error } = await fetchTeams();
  return (
    <div className="w-full p-4">
      <div className="gap-6 shadow-lg rounded-lg p-6">
        <div className="container mx-auto flex flex-col space-y-6">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-3xl md:text-4xl mb-4">
            NBA Teams
          </h2>
          <div>
            {error ? (
              <p className="text-red-500">Error when fetching teams: {error}</p>
            ) : !divisions ? (
              <p className="text-gray-500">Teams not found.</p>
            ) : (
              <DivisionTeamLists divisions={divisions} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
