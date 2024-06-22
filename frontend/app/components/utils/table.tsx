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

export default function TableComponent({ data, caption }: TableProps) {
  if (!data || data.length === 0) {
    return <div>No data available</div>;
  }

  const headers = Object.keys(data[0]);

  return (
    <Table className="table-auto w-full">
      <TableCaption>{caption}</TableCaption>
      <TableHeader>
        <TableRow>
          {headers.map((header, index) => (
            <TableHead key={index} className="px-4 py-2">{header}</TableHead>
          ))}
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((row, index) => (
          <TableRow key={index} className="border-t">
            {headers.map((header) => (
              <TableCell key={header} className="px-4 py-2">{row[header]}</TableCell>
            ))}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

// export default function TableComponent({ headers, data, caption }) {
//   return (
//     <Table>
//       <TableCaption>{caption}</TableCaption>
//       <TableHeader>
//         <TableRow>
//           {headers.map((header, index) => (
//           <TableHead key={index}>{header}</TableHead>
//           ))}
//         </TableRow>
//       </TableHeader>
//       <TableBody>
//         {data.map((row, index) => (
//           <TableRow key={index}>
//             {row.map((cell, index) => (
//               <TableCell key={index}>{cell}</TableCell>
//             ))}
//           </TableRow>
//         ))}
//       </TableBody>
//     </Table>
//   );
// }
