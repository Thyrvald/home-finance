// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import './App.css'
// import AddIncomeForm from "./components/AddIncomeForm";
// import AddCategoryForm from "./components/AddCategoryForm";
// import AddOneTimeExpenseForm from "./components/AddOneTimeExpenseForm.tsx";
//
// function App() {
//   const [count, setCount] = useState(0)
//
//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <div className="min-h-screen bg-gray-100 py-10">
//           <AddIncomeForm />
//       </div>
//       <div className="min-h-screen bg-gray-100 py-10">
//           <AddCategoryForm />
//       </div>
//         <div className="min-h-screen bg-gray-100 py-10">
//             <AddOneTimeExpenseForm />
//         </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 75)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.tsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }
//
// export default App

import Home from "./pages/Home";

function App() {
    return <Home />;
}

export default App;