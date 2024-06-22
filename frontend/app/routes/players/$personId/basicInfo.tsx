import { PlayerInfo } from "./types";

export default function BasicInfo({ player }: { player: PlayerInfo[] }) {
  const playerInfo = player[0];

  return (
    <div>
      <img
        src={playerInfo.IMAGE_URL}
        alt={playerInfo.DISPLAY_FIRST_LAST}
        style={{ width: "210px", height: "160px" }}
      />
      <p>HEIGHT: {playerInfo.HEIGHT}</p>
      <p>WEIGHT: {playerInfo.WEIGHT}</p>
      <p>COLLEGE: {playerInfo.SCHOOL}</p>
      {/* TODO: Need to get team that drafted player */}
      <p>
        DRAFT INFO: {playerInfo.DRAFT_YEAR}: RD {player.DRAFT_ROUND}, PK:{" "}
        {playerInfo.DRAFT_NUMBER}
      </p>
      <p>STATUS: {playerInfo.ROSTERSTATUS}</p>
    </div>
  );
}
