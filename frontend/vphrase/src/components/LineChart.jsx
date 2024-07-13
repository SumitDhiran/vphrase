// src/components/TopMoviesByVotes.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const TopMoviesByVotes = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/movies/line_chart/')
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data', error));
    }, []);

    const chartData = {
        labels: data.map(movie => movie.movie),
        datasets: [
            {
                label: 'Votes',
                data: data.map(movie => movie.votes),
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
                tension: 0.1
            },
        ],
    };

    return <Line data={chartData} />;
};

export default TopMoviesByVotes;
