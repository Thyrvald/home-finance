import { useEffect, useState } from "react";

export function ListOneTimeExpenses({ reload }: { reload: boolean }) {
    const [oneTimeExpenses, setOneTimeExpenses] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                console.log("Odpalam useEffect z reload =", reload);
                fetch("http://localhost:8000/one-time-expenses")
                    .then((res) => res.json())
                    .then((data) => {
                        console.log("Dostałem z backendu:", data);
                        setOneTimeExpenses(Array.isArray(data) ? data : []);
                    });
                // setIncome(data);
            } catch (error) {
                console.error("Failed to fetch one time expenses:", error);
            }
        };

        fetchData();
    }, [reload]);

    return (
        <div>
            <h2 className="text-xl font-semibold mb-2">Lista wydatków</h2>
            <ul className="space-y-2">
                {oneTimeExpenses.map((item: any, index: number) => (
                    <li key={index} className="border p-2 rounded">
                        {item.name} - {item.amount} zł | Kategoria: {item.category_name} | data: {item.date}
                    </li>
                ))}
            </ul>
        </div>
    );
}