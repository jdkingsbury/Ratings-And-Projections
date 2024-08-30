export default function AboutMe() {
  return (
    <div className="w-full max-w-4xl mx-auto py-16 md:py-20 lg:py-24">
      <div className="px-6 md:px-8 lg:px-10">
        <div className="space-y-10">
          <div className="text-center">
            <h1 className="text-4xl font-bold tracking-tight sm:text-5xl animate-fadeIn">
              About Ratings and Projections App
            </h1>
          </div>
          <div className="grid gap-12 md:grid-cols-2">
            <div>
              <h2 className="text-2xl font-bold">
                Reason for Creating the App
              </h2>
              <p className="mt-4 text-lg leading-relaxed text-muted-foreground">
                I created the application as a fun platform that tracks players'
                and teams' performances and creates ratings for each player and
                team. The goal is to display accurate ratings similar to
                2K-style player ratings, all determined by player and team
                performances.
              </p>
            </div>
            <div>
              <h2 className="text-2xl font-bold">Key Features</h2>
              <ul className="mt-4 space-y-6 text-lg leading-relaxed text-muted-foreground">
                <li className="flex items-start gap-4">
                  <div className="bg-muted rounded-full w-10 h-10 flex items-center justify-center">
                    <InfoIcon className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Advanced Analytics</h3>
                    <p>
                      Comprehensive statistical analysis of player performance,
                      including advanced metrics and projections.
                    </p>
                  </div>
                </li>
                <li className="flex items-start gap-4">
                  <div className="bg-muted rounded-full w-10 h-10 flex items-center justify-center">
                    <TrendingUpIcon className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Trend Tracking</h3>
                    <p>
                      Monitor player performance trends over time to identify
                      emerging stars and potential breakouts.
                    </p>
                  </div>
                </li>
                <li className="flex items-start gap-4">
                  <div className="bg-muted rounded-full w-10 h-10 flex items-center justify-center">
                    <CalendarDaysIcon className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="font-semibold">Injury Tracking</h3>
                    <p>
                      Stay up-to-date on player injuries and their potential
                      impact on performance and projections.
                    </p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function CalendarDaysIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M8 2v4" />
      <path d="M16 2v4" />
      <rect width="18" height="18" x="3" y="4" rx="2" />
      <path d="M3 10h18" />
      <path d="M8 14h.01" />
      <path d="M12 14h.01" />
      <path d="M16 14h.01" />
      <path d="M8 18h.01" />
      <path d="M12 18h.01" />
      <path d="M16 18h.01" />
    </svg>
  );
}

function InfoIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
      <path d="M12 16v-4" />
      <path d="M12 8h.01" />
    </svg>
  );
}

function TrendingUpIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <polyline points="22 7 13.5 15.5 8.5 10.5 2 17" />
      <polyline points="16 7 22 7 22 13" />
    </svg>
  );
}
