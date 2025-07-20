// import { ReactNode } from "react";
// import { Link } from "react-router-dom";
//
// export default function Layout({ children }: { children: ReactNode }) {
//     return (
//         <div className="flex h-screen">
//             <aside className="w-1/4 bg-gray-100 p-4 shadow-md">
//                 <nav className="space-y-4">
//                     <Link to="/Income/add" className="block text-blue-600 hover:underline">Dodaj przychód</Link>
//                     <Link to="/Income/list" className="block text-blue-600 hover:underline">Lista przychodów</Link>
//                     <Link to="/one-time-expenses/add" className="block text-blue-600 hover:underline">Dodaj wydatek</Link>
//                     <Link to="/one-time-expenses/list" className="block text-blue-600 hover:underline">Lista wydatków</Link>
//                     <Link to="/balance" className="block text-blue-600 hover:underline">Bilans</Link>
//                 </nav>
//             </aside>
//             <main className="flex-1 p-8 overflow-auto">
//                 {children}
//             </main>
//         </div>
//     );
// }

import { NavLink } from "react-router-dom";

export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <div className="flex h-screen">
            <aside className="w-1/4 bg-gray-100 p-4 shadow-md">
                <nav className="space-y-4">
                    <NavLink
                        to="/income/add"
                        className={({ isActive }) =>
                            isActive
                                ? "block font-bold text-white bg-blue-500 px-3 py-1 rounded"
                                : "block text-blue-600 hover:underline"
                        }
                    >
                        Dodaj przychód
                    </NavLink>
                    <NavLink
                        to="/income/list"
                        className={({ isActive }) =>
                            isActive
                                ? "block font-bold text-white bg-blue-500 px-3 py-1 rounded"
                                : "block text-blue-600 hover:underline"
                        }
                    >
                        Lista przychodów
                    </NavLink>
                    <NavLink
                        to="/one-time-expenses/add"
                        className={({ isActive }) =>
                            isActive
                                ? "block font-bold text-white bg-blue-500 px-3 py-1 rounded"
                                : "block text-blue-600 hover:underline"
                        }
                    >
                        Dodaj wydatek
                    </NavLink>
                    <NavLink
                        to="/one-time-expenses/list"
                        className={({ isActive }) =>
                            isActive
                                ? "block font-bold text-white bg-blue-500 px-3 py-1 rounded"
                                : "block text-blue-600 hover:underline"
                        }
                    >
                        Lista wydatków
                    </NavLink>
                    <NavLink
                        to="/balance"
                        className={({ isActive }) =>
                            isActive
                                ? "block font-bold text-white bg-blue-500 px-3 py-1 rounded"
                                : "block text-blue-600 hover:underline"
                        }
                    >
                        Bilans
                    </NavLink>
                </nav>
            </aside>
            <main className="flex-1 p-8 overflow-auto">
                {children}
            </main>
        </div>
    );
}