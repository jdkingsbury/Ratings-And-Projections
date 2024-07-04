import PlayerBio from "./basic-info.tsx"

async function PlayerInfo(personId) {
  const response = await fetch(
    `http://127.0.0.1:8000/nba/players/${personId}/player-info`,
  );
  return response.json();
}

async function CareerStats(personId) {
  const response = await fetch(
    `http://127.0.0.1:8000/nba/players/${personId}/career-stats`,
  );
  return response.json();
}

export default async function PlayerProfile({
  params,
}: {
  params: { personId: string };
}) {
  const [playerInfo, careerStats] = await Promise.all([
    PlayerInfo(params.personId),
    CareerStats(params.personId),
  ]);

  console.log(playerInfo);

  return (
    <div>
      <h1>Player Profile</h1>
    </div>
  );
}
