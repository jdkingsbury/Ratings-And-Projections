import { Player } from "./types";

// TODO: Finish updating the player profile page without the players image
// Will probably need to update the api endpoint to send the correct data
export function PlayerInfo({ data }: { data: Player }) {
  const birthdate = data.birth_date
    ? new Date(data.birth_date).toLocaleDateString()
    : "Unknown";

  return (
    <div className="w-full p-6 pb-0 flex justify-center">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-center md:text-left items-start">
        {/* Name */}
        <div className="flex flex-col items-center md:items-start">
          <span className="text-4xl font-light">{data.first_name}</span>
          <span className="text-3xl font-bold mt-1 md:mt-0">
            {data.last_name}
          </span>
        </div>
        {/* Jersey and team */}
        <div className="space-y-2 text-gray-700 dark:text-gray-400">
          <p className="text-sm font-medium">TEAM: {data.team_name}</p>
          <p className="text-sm font-medium">JERSEY: #{data.jersey}</p>
          <p className="text-sm font-medium">POSITION: {data.position}</p>
          <p className="text-sm font-medium">STATUS: {data.is_active}</p>
        </div>
        {/* Player Info including weight height draft */}
        <div className="space-y-2 text-gray-700 dark:text-gray-400">
          <p className="text-sm">HEIGHT: {data.height}</p>
          <p className="text-sm">WEIGHT: {data.weight}lb</p>
          <p className="text-sm">AGE: </p>
          <p className="text-sm">BORN: {birthdate}</p>
        </div>
        <div className="space-y-2 text-gray-700 dark:text-gray-400">
          <p className="text-sm">COLLEGE: {data.school}</p>
          <p className="text-sm">
            DRAFT INFO: {data.draft_year} | ROUND: {data.draft_round}, PICK:{" "}
            {data.draft_number}
          </p>
        </div>
        {/* Player Rating */}
      </div>
    </div>
  );
}
