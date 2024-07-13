// src/components/TopMoviesByRating.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Pie } from 'react-chartjs-2';

const TopMoviesByRating = ({ year }) => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get(`http://localhost:8000/movies/chart/?year=${year}`)
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data', error));
    }, [year]);

    const chartData = {
        labels: data.map(movie => movie.movie),
        datasets: [
            {
                label: 'Rating',
                data: data.map(movie => movie.rating),
                backgroundColor: [
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)'
                ],
            },
        ],
    };

    return <Pie data={chartData} />;
};

export default TopMoviesByRating;
