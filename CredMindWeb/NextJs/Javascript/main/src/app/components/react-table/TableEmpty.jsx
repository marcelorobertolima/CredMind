'use client';
import * as React from 'react';
import {
    TableContainer,
    Table,
    TableRow,
    TableCell,
    TableBody,
    Typography,
    TableHead,
    Box,
    Grid,
    FormLabel
} from '@mui/material';
import CustomTextField from '@/app/components/forms/theme-elements/CustomTextField';
import DownloadCard from '@/app/components/shared/DownloadCard';

import {
    createColumnHelper,
    flexRender,
    getCoreRowModel,
    useReactTable,
} from '@tanstack/react-table';



const columnHelper = createColumnHelper();

const columns = [
    columnHelper.accessor('imgsrc', {
        header: () => 'Users'
    }),
    columnHelper.accessor('pname', {
        header: () => 'Project Name',
    }),
    columnHelper.accessor('teams', {
        header: () => 'Team',
    }),
    columnHelper.accessor('status', {
        header: () => 'Status',
    }),
    columnHelper.accessor('budget', {
        header: () => 'Budget',
    }),
];

const TableEmpty = () => {
    const [data, _setData] = React.useState(() => []);

    const table = useReactTable({
        data,
        columns,
        getCoreRowModel: getCoreRowModel(),
    });

    const handleDownload = () => {
        const headers = ["Users", "Project Name", "Team", "Status", "Budget"];
        const rows = data.map(item => [

            item.name,
            item.pname,
            item.teams.map(team => team.text).join(", "),
            item.status,
            item.budget,
        ]);

        const csvContent = [
            headers.join(","),
            ...rows.map(e => e.join(","))
        ].join("\n");

        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "table-data.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        (<DownloadCard title="Empty Table" onDownload={handleDownload}>
            <Grid container spacing={3}>
                <Grid size={12}>
                    <Box>
                        <CustomTextField
                            type="text"
                            placeholder="search 0 records..."
                            onChange={(e) => handleSearchChange(e.target.value)}
                            sx={{
                                marginLeft: "10px",
                                marginTop: "13px"
                            }}
                        />
                        <TableContainer>
                            <Table
                                sx={{
                                    whiteSpace: 'nowrap',
                                }}
                            >
                                <TableHead>
                                    {table.getHeaderGroups().map((headerGroup) => (
                                        <TableRow key={headerGroup.id}>
                                            {headerGroup.headers.map((header) => (
                                                <TableCell key={header.id}>
                                                    <Typography variant="h6">
                                                        {header.isPlaceholder
                                                            ? null
                                                            : (
                                                                <>
                                                                    <FormLabel
                                                                        sx={{
                                                                            marginBottom: "7px",
                                                                            display: "block"
                                                                        }}
                                                                    >{flexRender(header.column.columnDef.header, header.getContext())}</FormLabel>
                                                                    <CustomTextField
                                                                        type="text"
                                                                        placeholder={`Search ${header.id}`}
                                                                        onChange={(e) => handleSearchChange(header.id, e.target.value)}
                                                                    />
                                                                </>
                                                            )}
                                                    </Typography>
                                                </TableCell>
                                            ))}
                                        </TableRow>
                                    ))}
                                </TableHead>
                                <TableBody>
                                    <TableRow>
                                        <TableCell colSpan={columns.length}>
                                            <Box sx={{
                                                display: 'flex',
                                                alignItems: 'center',
                                                justifyContent: 'center',
                                                height: '200px',
                                            }}>
                                                <img
                                                    src="/images/svgs/no-data.webp"
                                                    alt="No data"
                                                    style={{
                                                        maxWidth: '100%',
                                                        maxHeight: '100%',
                                                    }}
                                                />
                                            </Box>
                                        </TableCell>
                                    </TableRow>
                                    {table.getHeaderGroups().map((headerGroup) => (
                                        <TableRow key={headerGroup.id}>
                                            {headerGroup.headers.map((header) => (
                                                <TableCell key={header.id}>
                                                    <Typography variant="h6">
                                                        {header.isPlaceholder
                                                            ? null
                                                            : flexRender(header.column.columnDef.header, header.getContext())}
                                                    </Typography>
                                                </TableCell>
                                            ))}
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </Box>
                </Grid>
            </Grid>
        </DownloadCard>)
    );
};

export default TableEmpty;
