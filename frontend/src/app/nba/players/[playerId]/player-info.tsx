import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Player } from "./types";
import Image from "next/image";

export function PlayerInfo({ data }: { data: Player }) {
  const playerInfo = data;
  console.log(playerInfo.height);

  const birthdate = playerInfo.birth_date
    ? new Date(playerInfo.birth_date).toLocaleDateString()
    : "Unknown";

  return (
    <div className="w-full p-4">
      <Card className="gap-6 shadow-sm rounded-lg">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 items-center text-center md:text-left">
          {/* Player Image */}
          <div className="w-full md:w-[380px] h-[175px] mx-auto">
            <Image
              src={playerInfo.image_url}
              alt={playerInfo.first_last}
              quality={100}
              width={240}
              height={200}
              className="rounded-md object-cover mr-6"
            />
          </div>
          {/* Name Jersey and team */}
          <div className="md:col-span-1 px-4 md:px-0">
            <h2 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white">
              {playerInfo.first_last}
            </h2>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              TEAM: {playerInfo.team_id}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              JERSEY: {"#"}
              {playerInfo.jersey}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              POSITION: {playerInfo.position}
            </p>
          </div>
          {/* Player Info including weight height draft */}
          <div className="md:col-span-1 pl-0 md:pl-6 border-t md:border-t-0 pt-4 md:pt-0 dark:text-white">
            <p className="mt-2 text-gray-700 text-sm dark:text-white">
              HEIGHT: {playerInfo.height}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              WEIGHT: {playerInfo.weight}lb
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">AGE: </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              BORN: {birthdate}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              COLLEGE: {playerInfo.school}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              DRAFT INFO: {playerInfo.draft_year} | ROUND:{" "}
              {playerInfo.draft_round}, PICK: {playerInfo.draft_number}
            </p>
            <p className="mt-1 text-sm">STATUS: {playerInfo.is_active}</p>
          </div>
          {/* Player Rating */}
        </div>
      </Card>
    </div>
  );
}
