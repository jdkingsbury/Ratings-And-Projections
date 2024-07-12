"use client";

import React from "react";
import { useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { buttonVariants } from "@/components/ui/button";
import { ThemeToggle } from "@/components/ThemeToggle";
import { Menu } from "lucide-react";
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu";

export default function Component() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="fixed inset-x-0 top-0 z-50 border-b">
      <div className="w-full max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-14 items-center">
          {/* Logo: Link to Home */}
          <Link href="/" className="flex items-center gap-2" prefetch={false}>
            <TestTubeIcon className="h-6 w-6 text-primary" />
            <span className="text-lg font-semibold">Sports Predictions</span>
          </Link>
          {/* Desktop Navigation */}
          <div className="hidden md:flex gap-4">
            {/* Link to Home */}
            <Link
              href="/"
              // className="font-medium flex items-center text-sm transition-colors hover:underline"
              className={buttonVariants({ variant: "ghost" })}
              prefetch={false}
            >
              Home
            </Link>
            {/* Drop Down for NBA */}
            <NavigationMenu>
              <NavigationMenuList>
                <NavigationMenuItem>
                  <NavigationMenuTrigger>NBA</NavigationMenuTrigger>
                  <NavigationMenuContent>
                    {/* Link to Player Page */}
                    <Link href="/players" prefetch={false}>
                      <NavigationMenuLink
                        className={navigationMenuTriggerStyle()}
                      >
                        Players
                      </NavigationMenuLink>
                    </Link>
                  </NavigationMenuContent>
                </NavigationMenuItem>
              </NavigationMenuList>
            </NavigationMenu>
            {/* Link to About */}
            <Link
              href="about"
              // className="font-medium flex items-center text-sm transition-colors hover:underline"
              className={buttonVariants({ variant: "ghost" })}
              prefetch={false}
            >
              About
            </Link>
          </div>
          {/* Mobile Menu Button */}
          <button
            className="md:hidden flex items-center"
            onClick={toggleMobileMenu}
          >
            <Menu className="h-6 w-6" />
          </button>

          {/* Mobile Menu */}
          {isMobileMenuOpen && (
            <div className="md:hidden absolute top-14 left-0 right-0 bg-white dark:bg-gray-950/90 shadow-sm z-50">
              <div className="flex flex-col gap-4 p-4">
                {/* Link to Home */}
                <Link
                  href="/"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  Home
                </Link>
                {/* Link to Players */}
                <Link
                  href="/players"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  Players
                </Link>
                {/* Link to NBA */}
                <Link
                  href="/nba"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  NBA
                </Link>
                {/* Link to About */}
                <Link
                  href="/about"
                  className="font-medium text-sm transition-colors hover:underline"
                  prefetch={false}
                  onClick={toggleMobileMenu}
                >
                  About
                </Link>
              </div>
            </div>
          )}
          <div className="flex items-center gap-4">
            <ThemeToggle className="ml-4" />
          </div>
        </div>
      </div>
    </nav>
  );
}

function TestTubeIcon(props: React.SVGProps<SVGSVGElement>) {
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
      <path d="M14.5 2v17.5c0 1.4-1.1 2.5-2.5 2.5h0c-1.4 0-2.5-1.1-2.5-2.5V2" />
      <path d="M8.5 2h7" />
      <path d="M14.5 16h-5" />
    </svg>
  );
}

function TrophyIcon(props: React.SVGProps<SVGSVGElement>) {
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
      <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6" />
      <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18" />
      <path d="M4 22h16" />
      <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22" />
      <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22" />
      <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z" />
    </svg>
  );
}
