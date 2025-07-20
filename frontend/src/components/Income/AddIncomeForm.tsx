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