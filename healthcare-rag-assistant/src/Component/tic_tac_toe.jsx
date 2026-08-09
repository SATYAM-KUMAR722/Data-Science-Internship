import { useState } from 'react';

export default function tic_tac_toe() {

const [board, serBoard] = useState(Array(9).fill(null));
const [xIsNext, setXIsNext] = useState(true);
const[winner, setWinner] = useState(null);

const renderSquare = (index) => {
  return <button className='button' onClick={()=> handleClick(index)}>{board[index]}</button>
}

const handleClick = (index) => {
  if(board[index] != null) {
    return;
  }
  console.log(index, " Clicked")
  const newBoard = [...board]
  newBoard[index] = xIsNext ? 'X' : 'O'
  serBoard(newBoard)
  setXIsNext(!xIsNext)
  const winningCombo = checkWinner(newBoard);
  if(winningCombo){
    setWinner(newBoard[winningCombo[0]]);
  }
}

const checkWinner = (board) => {
  const combination = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [1, 5, 7],
    [2, 5, 8],
  ]
    for(let i=0; i<combination.length; i++) {
     const [a,b,c] = combination[i];
      if(board[a] === board[b] && board[b] === board[c] && board[a] === board[c]) {
        return combination[i];
      }
    }
    return null;
  
}

  return (
    <>
    
    <div className='board'>
      <div className='board_row'>
        {renderSquare(0)}
        {renderSquare(1)}
        {renderSquare(2)}
      </div>
       <div className='board_row'>
        {renderSquare(3)}
        {renderSquare(4)}
        {renderSquare(5)}
      </div>
       <div className='board_row'>
        {renderSquare(6)}
        {renderSquare(7)}
        {renderSquare(8)}
      </div>
    </div>

    {winner && <div>{winner} "is the Winner of the Game"</div>}
    </>
  )
}
