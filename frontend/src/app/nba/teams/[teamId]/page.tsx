import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import { Team } from "../types";
import axios from "axios";
import { Card, CardContent } from "@/components/ui/card";
import { TeamInfo } from "./team-info";

// Ideas for the Team Profile Page:
// - Team Roster
// - Team Standings
// - Season Record
// - Schedule
// - Rating
// - Injuries

type FetchTeamInfo = {
  data: Team | null;
  error: string | null;
};

async function fetchTeamInfo(teamId: string): Promise<FetchTeamInfo> {
  try {
    const response = await axios.get<Team>(
      `${BACKEND_API_BASE_URL}/nba/teams/${teamId}`,
    );
    return { error: null, data: response.data };
  } catch (error: any) {
    console.error(`Failed to fetch team info: {error.message}`);
    return { error: error.message, data: null };
  }
}

export default async function TeamProfile({
  params,
}: {
  params: { teamId: string };
}) {
  const teamInfo = await fetchTeamInfo(params.teamId);

  try {
    return (
      <div className="p-6 min-h-screen">
        <div className="mb-6">
          <Card className="p-4 shadow-md rounded-lg w-full">
            <CardContent>
              {teamInfo.error ? (
                <p className="text-red-500">
                  Error when fetching team info: {teamInfo.error}
                </p>
              ) : !teamInfo.data ? (
                <p className="text-gray-500">Team not found.</p>
              ) : (
                <TeamInfo data={teamInfo.data} />
              )}
            </CardContent>
          </Card>
        </div>
      </div>
    );
  } catch (error) {
    console.error("Failed to fetch team info:", error);
    return <div>Error loading team info</div>;
  }
}
