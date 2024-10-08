// Team Name
// Record
// Rank in Conference
// PPG
// RPG
// APG
// OPPG

import { Team } from "../types";

export function TeamInfo({ data }: { data: Team }) {
  return (
    <div className="w-full p-6 pb-0 flex justify-center">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-center md:text-left items-start">
        {/* Team Name */}
        <div className="flex flex-col items-center md:items-start">
          <span className="text-4xl font-light">{data.city}</span>
          <span className="text-3xl font-bold mt-1 md:mt-0">
            {data.nickname}
          </span>
        </div>
        {/* Record and Conference Standing */}
        <div className="space-y-2 text-gray-700 dark:text-gray-400">
          <p className="text-sm font-medium">
            RECORD: {data.w} - {data.l}
          </p>
          <p className="text-sm font-medium">
            CONFERENCE: {data.conf_rank}st in {data.conference}
          </p>
          <p className="text-sm font-medium">
            DIVISION: {data.div_rank}st in {data.division}
          </p>
        </div>
        {/* PPG */}
      </div>
    </div>
  );
}
