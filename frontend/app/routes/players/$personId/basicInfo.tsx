import { AspectRatio } from "~/components/ui/aspect-ratio";
import { PlayerInfo } from "./types";

export default function BasicInfo({ player }: { player: PlayerInfo[] }) {
  const playerInfo = player[0];

  const birthdate = new Date(playerInfo.BIRTHDATE);
  const formattedBirthdate = birthdate.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  return (
    <div className="flex flex-col md:flex-row items-center bg-white p-6 rounded-lg shadow-md">
      <div className="w-[350px]">
        <AspectRatio ratio={16 / 9}>
          <img src={playerInfo.IMAGE_URL} className="rounded-md object-cover" />
        </AspectRatio>
      </div>
      <div className="text-left">
        <h2 className="text-2xl font-bold">{playerInfo.DISPLAY_FIRST_LAST}</h2>
        <p className="mt-1 text-gray-600 text-sm">
          TEAM: {playerInfo.TEAM_NAME}
        </p>
        <p className="mt-1 text-gray-600 text-sm">
          JERSEY: {"#"}
          {playerInfo.JERSEY}
        </p>
        <p className="mt-1 text-gray-600 text-sm">
          POSITION: {playerInfo.POSITION}
        </p>
        <p className="mt-1 text-gray-600 text-sm">
          HEIGHT: {playerInfo.HEIGHT}
        </p>
        <p className="mt-1 text-gray-600 text-sm">
          WEIGHT: {playerInfo.WEIGHT}lb
        </p>
        <p className="mt-1 text-gray-600 text-sm">AGE: </p>
        <p className="mt-1 text-gray-600 text-sm">BORN: {formattedBirthdate}</p>
        <p className="mt-1 text-gray-600 text-sm">COUNTRY: {playerInfo.COUNTRY}</p>
        {/* TODO: Get Player hometown */}
        <p className="mt-1 text-gray-600 text-sm">HOMETOWN: </p>
        <p className="mt-1 text-gray-600 text-sm">
          COLLEGE: {playerInfo.SCHOOL}
        </p>
        {/* TODO: Get team that drafted the player */}
        <p className="mt-1 text-gray-600 text-sm">
          DRAFT INFO: {playerInfo.DRAFT_YEAR} | ROUND: {playerInfo.DRAFT_ROUND}, PICK:{" "}
          {playerInfo.DRAFT_NUMBER}
        </p>
        <p className="mt-1 text-gray-600 text-sm">
          STATUS: {playerInfo.ROSTERSTATUS}
        </p>
      </div>
    </div>
  );
}
