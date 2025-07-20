import { useEffect, useState } from "react";

export function GetBalance({ reload }: { reload: boolean }) {
    const [balance, setBalance] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                console.log("Odpalam useEffect z reload =", reload);
                fetch("http://localhost:8000/balance")
                    .then((res) => res.json())
                    .then((data) => {
                        console.log("Dostałem z backendu:", data);
                        setBalance(Array.isArray(data) ? data : []);
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
            <h2 className="text-xl font-semibold mb-2">Bilans</h2>
            <ul className="space-y-2">
                {balance.map((item: any, index: number) => (
                    <li key={index} className="border p-2 rounded">
                        Bilans - {item.amount} zł
                    </li>
                ))}
            </ul>
        </div>
    );
}