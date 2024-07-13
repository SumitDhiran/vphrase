// src/components/YearDropdown.js
import React from 'react';

const YearDropdown = ({ years, selectedYear, onSelectYear }) => {
    return (
        <select value={selectedYear} onChange={(e) => onSelectYear(e.target.value)}>
            {years.map(year => (
                <option key={year} value={year}>
                    {year}
                </option>
            ))}
        </select>
    );
};

export default YearDropdown;
