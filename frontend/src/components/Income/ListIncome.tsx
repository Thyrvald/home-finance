import { useEffect, useState } from "react";

export function ListIncome({ reload }: { reload: boolean }) {
    const [income, setIncome] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                console.log("Odpalam useEffect z reload =", reload);
                fetch("http://localhost:8000/income")
                    .then((res) => res.json())
                    .then((data) => {
                        console.log("Dostałem z backendu:", data);
                        setIncome(Array.isArray(data) ? data : []);
                    });
                // setIncome(data);
            } catch (error) {
                console.error("Failed to fetch Income:", error);
            }
        };

        fetchData();
    }, [reload]);

    return (
        <div>
            <h2 className="text-xl font-semibold mb-2">Lista przychodów</h2>
            <ul className="space-y-2">
                {income.map((item: any, index: number) => (
                    <li key={index} className="border p-2 rounded">
                        {item.name} - {item.amount} zł
                    </li>
                ))}
            </ul>
        </div>
    );
}