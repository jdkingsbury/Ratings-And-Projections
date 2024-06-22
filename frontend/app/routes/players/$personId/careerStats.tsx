import TableComponent from "~/components/utils/table";
import { CareerStats } from "./types";

export default function PlayerCareerStats({ player }: { player: CareerStats[] }) {
  return (
    <div>
      <h1>Player Career Stats</h1>
      <TableComponent data={player} caption="Player Career Stats" />
    </div>
  );
}
