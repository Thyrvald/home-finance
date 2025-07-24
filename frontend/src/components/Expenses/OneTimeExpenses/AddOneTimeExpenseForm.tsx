// src/components/AddIncomeForm.tsx
import {useEffect, useState} from "react";

export function AddOneTimeExpenseForm({ onAdd }: { onAdd: () => void }) {
    const [name, setName] = useState("");
    const [amount, setAmount] = useState("");
    const [date, setDate] = useState("");
    const [categoryId, setCategoryId] = useState("");
    const [categories, setCategories] = useState([]);
    const [message, setMessage] = useState("");

    //Get categories

    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const res = await fetch("http://localhost:8000/category/");
                const data = await res.json();
                setCategories(data);
            } catch (err) {
                console.error("Błąd pobierania kategorii:", err);
            }
        };
        fetchCategories();
    }, []);

    //Send request

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setMessage("Wysyłanie...");

        try {
            const res = await fetch("http://localhost:8000/one-time-expenses/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    name,
                    date,
                    amount: parseFloat(amount),
                    category_id: parseInt(categoryId),
                }),
            });

            if (!res.ok) throw new Error("Błąd przy dodawaniu");

            setMessage("✅ Wydatek dodany pomyślnie");
            setName("");
            setAmount("");
            setDate("")
            setCategoryId("")
            console.log("Dodano przychód, wywołuję onAdd()");
            onAdd(); // odświeżenie listy
        } catch (err) {
            console.error(err);
            setMessage("❌ Wystąpił błąd");
        }
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="max-w-md mx-auto p-4 bg-white shadow rounded-lg space-y-4"
        >
            <h2 className="text-xl font-bold">Dodaj wydatek</h2>

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

            <div>
                <label className="block mb-1 font-medium">Kwota</label>
                <input
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                    required
                    className="w-full p-2 border rounded"
                />
            </div>

            <div>
                <label className="block mb-1 font-medium">Data</label>
                <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                    className="w-full p-2 border rounded"
                />
            </div>

            <div>
                <label className="block mb-1 font-medium">Kategoria</label>
                <select
                    value={categoryId}
                    onChange={(e) => setCategoryId(e.target.value)}
                    required
                    className="w-full p-2 border rounded"
                >
                    <option value="">-- Wybierz kategorię --</option>
                    {categories.map((category: any) => (
                        <option key={category.id} value={category.id}>
                            {category.name}
                        </option>
                    ))}
                </select>
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