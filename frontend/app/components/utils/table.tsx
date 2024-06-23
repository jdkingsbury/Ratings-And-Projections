import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "~/components/ui/table";

interface TableProps {
  data: Record<string, any>[];
  caption: string;
}

// TODO: Find a way to fix the size of the table

export default function TableComponent({ data, caption }: TableProps) {
  if (!data || data.length === 0) {
    return <div>No data available</div>;
  }

  const headers = Object.keys(data[0]);

  return (
    <div className="overflow-x-auto">
      <Table className="table-auto border-collapse border-l border-r border border-gray-300 mx-auto rounded-lg">
        <TableCaption>{caption}</TableCaption>
        <TableHeader>
          <TableRow>
            {headers.map((header, index) => (
              <TableHead key={index} className="px-4 py-2">
                {header}
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {data.map((row, index) => (
            <TableRow key={index} className="border-t">
              {headers.map((header) => (
                <TableCell key={header} className="px-4 py-2">
                  {row[header]}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
