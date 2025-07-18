import { ReactNode } from "react";
import { Link } from "react-router-dom";

export default function Layout({ children }: { children: ReactNode }) {
    return (
        <div className="flex h-screen">
            <aside className="w-1/4 bg-gray-100 p-4 shadow-md">
                <nav className="space-y-4">
                    <Link to="/income/add" className="block text-blue-600 hover:underline">Dodaj przychód</Link>
                    <Link to="/income/list" className="block text-blue-600 hover:underline">Lista przychodów</Link>
                    <Link to="/balance" className="block text-blue-600 hover:underline">Bilans</Link>
                </nav>
            </aside>
            <main className="flex-1 p-8 overflow-auto">
                {children}
            </main>
        </div>
    );
}