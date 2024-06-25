import TableComponent from "~/components/utils/table";

export default function PreviousGames({ games }) {
  return (
    <div className="container mx-auto py-10 px-4 sm:px-6">
      <h1 className="font-bold mb-4">Recent Games</h1>
      <div className="overflow-x-auto">
        <TableComponent
          data={games}
          className="min-w-full divide-y divide-gray-200"
        />
      </div>
    </div>
  );
}
