import { AspectRatio } from "@/components/ui/aspect-ratio";
import { Card, CardContent, CardHeader } from "@/components/ui/card";

export function PlayerBio({ data }) {
  const playerInfo = data[0];

  const birthdate = new Date(
    playerInfo.BIRTHDATE as string,
  ).toLocaleDateString();

  return (
    <div className="w-full p-4">
      <Card className= "gap-6 shadow-sm rounded-lg">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 items-center text-center md:text-left">
          {/* Player Image */}
          <div className="w-full md:w-[350px] h-[190px] mx-auto">
            <AspectRatio ratio={16 / 9}>
              <img
                src={playerInfo.IMAGE_URL}
                className="rounded-md object-cover mr-6"
              />
            </AspectRatio>
          </div>
          {/* Name Jersey and team */}
          <div className="md:col-span-1 px-4 md:px-0">
            <h2 className="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white">
              {playerInfo.DISPLAY_FIRST_LAST}
            </h2>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              TEAM: {playerInfo.TEAM_NAME}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              JERSEY: {"#"}
              {playerInfo.JERSEY}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              POSITION: {playerInfo.POSITION}
            </p>
          </div>
          {/* Player Info including weight height draft */}
          <div className="md:col-span-1 pl-0 md:pl-6 border-t md:border-t-0 pt-4 md:pt-0 dark:text-white">
            <p className="mt-2 text-gray-700 text-sm dark:text-white">
              HEIGHT: {playerInfo.HEIGHT}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              WEIGHT: {playerInfo.WEIGHT}lb
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">AGE: </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              BORN: {birthdate}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              COLLEGE: {playerInfo.SCHOOL}
            </p>
            <p className="mt-1 text-gray-700 text-sm dark:text-white">
              DRAFT INFO: {playerInfo.DRAFT_YEAR} | ROUND:{" "}
              {playerInfo.DRAFT_ROUND}, PICK: {playerInfo.DRAFT_NUMBER}
            </p>
            <p className="mt-1 text-sm">STATUS: {playerInfo.ROSTERSTATUS}</p>
          </div>
          {/* Player Rating */}
        </div>
      </Card>
    </div>
  );
}
