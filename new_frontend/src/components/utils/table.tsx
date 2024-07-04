import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Card, CardContent, CardHeader } from "@/components/ui/card";

interface TableProps {
  columns: Column[];
  data: any[];
  caption?: string;
}

export function TableComponent({ columns, data, caption }: TableProps) {
  return (
    <div className="w-full overflow-x-auto">
      <Card className="min-w-full shadow-sm rounded-lg overflow-hidden">
        {caption && (
          <CardHeader className= "p-4 rounded-t-lg">
            <h3 className="text-lg font-semibold">
              {caption}
            </h3>
          </CardHeader>
        )}
        <CardContent className="p-0">
          <Table className="min-w-full border-t">
            <TableHeader>
              <TableRow>
                {columns.map((column) => (
                  <TableHead
                    key={column.accessorKey}
                    className="px-2 md:px-4 py-3 text-left text-xs font-medium uppercase tracking-wider"
                  >
                    {column.header}
                  </TableHead>
                ))}
              </TableRow>
            </TableHeader>
            <TableBody>
              {data.map((row, rowIndex) => (
                <TableRow key={rowIndex} className="border-t">
                  {columns.map((column) => (
                    <TableCell
                      key={column.accessorKey}
                      className="px-2 md:px-4 py-2 whitespace-nowrap text-sm"
                    >
                      {row[column.accessorKey]}
                    </TableCell>
                  ))}
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
