import { PlayerInfo } from "./types";

export default function BasicInfo({ player }: { player: PlayerInfo[] }) {
  const playerInfo = player[0];

  return (
    <div className="flex flex-col md:flex-row items-center bg-white p-6 rounded-lg shadow-md">
      <img
        src={playerInfo.IMAGE_URL}
        alt={playerInfo.DISPLAY_FIRST_LAST}
        style={{ width: "210px", height: "160px" }}
      />
      <div className="text-left">
        <h2 className="text-2xl font-bold">{playerInfo.DISPLAY_FIRST_LAST}</h2>
        <p className="mt-2 text-gray-600">HEIGHT: {playerInfo.HEIGHT}</p>
        <p className="mt-2 text-gray-600">WEIGHT: {playerInfo.WEIGHT}</p>
        <p className="mt-2 text-gray-600">COLLEGE: {playerInfo.SCHOOL}</p>
        {/* TODO: Need to get team that drafted them */}
        <p className="mt-2 text-gray-600">
          DRAFT INFO: {playerInfo.DRAFT_YEAR}: RD {playerInfo.DRAFT_ROUND}, PK:{" "}
          {playerInfo.DRAFT_NUMBER}
        </p>
        <p className="mt-1 text-gray-600">STATUS: {playerInfo.ROSTERSTATUS}</p>
      </div>
    </div>
  );
}
