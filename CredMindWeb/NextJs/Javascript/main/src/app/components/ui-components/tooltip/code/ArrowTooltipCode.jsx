import CodeDialog from "@/app/components/shared/CodeDialog";
import React from "react";
const ArrowTooltipCode = () => {
    return (
        <>
            <CodeDialog>
                {`
"use client";
import * as React from 'react';
import { Fab, Box } from '@mui/material';
import Tooltip from '@mui/material/Tooltip';
import { IconPlus } from '@tabler/icons-react';

 <Box sx={{
            textAlign: "center"
        }}>
    <Tooltip title="Delete" arrow>
        <Fab color="secondary">
            <IconPlus width={20} height={20} />
        </Fab>
    </Tooltip>
</Box>
`}
            </CodeDialog>
        </>
    );
};

export default ArrowTooltipCode;
