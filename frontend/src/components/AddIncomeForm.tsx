// // src/components/AddIncomeForm.tsx
// import { useState } from "react";
//
// export default function AddIncomeForm() {
//     const [name, setName] = useState("");
//     const [amount, setAmount] = useState("");
//     const [message, setMessage] = useState("");
//
//     const handleSubmit = async (e: React.FormEvent) => {
//         e.preventDefault();
//         setMessage("Wysyłanie...");
//
//         try {
//             const res = await fetch("http://127.0.0.1:8000/income", {
//                 method: "POST",
//                 headers: {
//                     "Content-Type": "application/json",
//                 },
//                 body: JSON.stringify({
//                     name,
//                     amount: parseFloat(amount),
//                 }),
//             });
//
//             if (!res.ok) throw new Error("Błąd przy dodawaniu");
//
//             setMessage("✅ Przychód dodany pomyślnie");
//             setName("");
//             setAmount("");
//         } catch (err) {
//             console.error(err);
//             setMessage("❌ Wystąpił błąd");
//         }
//     };
//
//     return (
//         <form
//             onSubmit={handleSubmit}
//             className="max-w-md mx-auto p-4 bg-white shadow rounded-lg space-y-4"
//         >
//             <h2 className="text-xl font-bold">Dodaj przychód</h2>
//
//             <div>
//                 <label className="block mb-1 font-medium">Nazwa</label>
//                 <input
//                     type="text"
//                     value={name}
//                     onChange={(e) => setName(e.target.value)}
//                     required
//                     className="w-full p-2 border rounded"
//                 />
//             </div>
//
//             <div>
//                 <label className="block mb-1 font-medium">Kwota</label>
//                 <input
//                     type="number"
//                     value={amount}
//                     onChange={(e) => setAmount(e.target.value)}
//                     required
//                     className="w-full p-2 border rounded"
//                 />
//             </div>
//
//             <button
//                 type="submit"
//                 className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded"
//             >
//                 Dodaj
//             </button>
//
//             {message && <p className="text-sm text-gray-700">{message}</p>}
//         </form>
//     );
// }

import { useState } from "react";

export function AddIncomeForm({ onAdd }: { onAdd: () => void }) {
    const [name, setName] = useState("");
    const [amount, setAmount] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await fetch("http://localhost:8000/income", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, amount: parseFloat(amount) }),
        });
        setName("");
        setAmount("");
        console.log("Dodano przychód, wywołuję onAdd()");
        onAdd(); // odświeżenie listy
    };

    return (
        <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
            <input
                className="border p-2 rounded w-1/3"
                placeholder="Nazwa"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
            />
            <input
                className="border p-2 rounded w-1/3"
                type="number"
                placeholder="Kwota"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                required
            />
            <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
                Dodaj
            </button>
        </form>
    );
}