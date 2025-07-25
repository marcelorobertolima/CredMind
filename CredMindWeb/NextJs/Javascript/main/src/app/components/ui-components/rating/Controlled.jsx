'use client';
import * as React from 'react';
import { Rating } from '@mui/material';
import ChildCard from '@/app/components/shared/ChildCard';

const Controlled = () => {
    const [value, setValue] = React.useState(2);

    return (

        <ChildCard title="Controlled">
            <Rating
                name="simple-controlled"
                value={value}
                onChange={(newValue) => {
                    setValue(newValue);
                }}
            />
        </ChildCard>

    );
};
export default Controlled;
