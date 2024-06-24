import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "~/components/ui/table";

interface TableProps {
  data: Record<string, any>[];
  className?: string;
}

// TODO: Find a way to fix the size of the table

export default function TableComponent({ data, className }: TableProps) {
  if (!data || data.length === 0) {
    return <div>No data available</div>;
  }

  const headers = Object.keys(data[0]);

  return (
    <div>
      <div className="overflow-x-auto">
        <Table className={`min-w-full bg-white border-t border-b ${className}`}>
          <TableHeader className="bg-gray-50">
            <TableRow>
              {headers.map((header, index) => (
                <TableHead key={index} className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  {header}
                </TableHead>
              ))}
            </TableRow>
          </TableHeader>
          <TableBody className="bg-white divide-y divide-gray-200">
            {data.map((row, index) => (
              <TableRow key={index} className="border-t">
                {headers.map((header) => (
                  <TableCell key={header} className="px-4 py-2 whitespace-nowrap text-sm text-gray-900">
                    {row[header]}
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
