// Ideas for the Team Profile Page:
// - Team Roster
// - Team Standings
// - Season Record
// - Schedule
// - Rating
// - Injuries

export default function TeamProfile({
  params,
}: {
  params: { teamId: string };
}) {
  return (
    <div className="p-6 min-h-screen">
      <div className="mb-6">Team Page</div>
    </div>
  );
}
