'use client';
import React from "react";
import { Box, Stack, Typography, Container, Grid, Button } from "@mui/material";
import Link from "next/link";

const Banner = () => {


    return (
        (<Box
            sx={{
                bgcolor: "primary.light",

                paddingTop: {
                    xs: '40px',
                    lg: '100px',
                },

                paddingBottom: {
                    xs: '40px',
                    lg: '100px',
                }
            }}>
            <Container maxWidth="lg">
                <Grid container spacing={3} sx={{
                    justifyContent: "space-between"
                }}>
                    <Grid
                        size={{
                            xs: 12,
                            lg: 6
                        }}
                        sx={{
                            alignItems: "center"
                        }}>
                        <Typography
                            variant="h1"
                            sx={{
                                mb: 3,
                                lineHeight: 1.4,
                                fontWeight: 700,

                                fontSize: {
                                    xs: '34px', sm: '48px'
                                }
                            }}>Get to know Modernize Dashboard Template</Typography>
                        <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2}>
                            <Button variant="contained" size="large" component={Link} href="/auth/auth1/register">Create an account</Button>
                            <Button variant="outlined" size="large">View Open Positions</Button>
                        </Stack>
                    </Grid>
                    <Grid
                        size={{
                            xs: 12,
                            lg: 5
                        }}
                        sx={{
                            display: "flex",
                            alignItems: "center"
                        }}>
                        <Typography sx={{
                            lineHeight: 1.9
                        }} >Do you need a highly customizable and developer friendly premium next.js admin template packed with numerous features? Modernize Next.js Admin Template has everything you need. This bootstrap based admin template is designed in accordance with industry standards and best practices to provide you.</Typography>
                    </Grid>
                </Grid>
            </Container>
        </Box>)
    );
};

export default Banner;
