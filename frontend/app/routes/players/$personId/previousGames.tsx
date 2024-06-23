import TableComponent from "~/components/utils/table";

export default function PreviousGames({ games }) {
  return (
    <div>
      <h1>Last 5 Games</h1>
      <TableComponent data={games} caption="Previous 5 Games" />
    </div>
  );
}
