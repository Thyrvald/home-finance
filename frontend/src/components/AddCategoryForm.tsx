// src/components/AddCategoryForm.tsx
import { useState } from "react";

export default function AddCategoryForm() {
    const [name, setName] = useState("");
    const [amount, setAmount] = useState("");
    const [message, setMessage] = useState("");

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setMessage("Wysyłanie...");

        try {
            const res = await fetch("http://127.0.0.1:8000/category", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    name,
                }),
            });

            if (!res.ok) throw new Error("Błąd przy dodawaniu");

            setMessage("✅ Kategoria dodana pomyślnie");
            setName("");
            setAmount("");
        } catch (err) {
            console.error(err);
            setMessage("❌ Wystąpił błąd");
        }
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="max-w-md mx-auto p-4 bg-grey shadow rounded-lg space-y-4"
        >
            <h2 className="text-xl font-bold">Dodaj Kategorię</h2>

            <div>
                <label className="block mb-1 font-medium">Nazwa</label>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                    className="w-full p-2 border rounded"
                />
            </div>

            <button
                type="submit"
                className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded"
            >
                Dodaj
            </button>

            {message && <p className="text-sm text-gray-700">{message}</p>}
        </form>
    );
}