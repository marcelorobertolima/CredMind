'use client';
import React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import CardContent from '@mui/material/CardContent';
import Container from '@mui/material/Container';
import { Grid } from '@mui/material';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';
import BlankCard from '../../shared/BlankCard';
import AnimationFadeIn from '../animation/Animation';

const ImgCard = styled(BlankCard)(() => ({
  backgroundImage: `url('/images/landingpage/shape/line-bg.svg')`,
  backgroundRepeat: 'no-repeat',
  backgroundPosition: 'center center',
}));

const StyledButton = styled(Button)(() => ({
  padding: '13px 48px',
  fontSize: '16px',
}));

const StyledButton2 = styled(Button)(({ theme }) => ({
  padding: '13px 48px',
  fontSize: '16px',
  background: theme.palette.background.paper,
}));

const C2a = () => {
  return (
    (<Box
      sx={{
        pt: 7,

        pb: {
          xs: '70px',
          lg: '120px',
        }
      }}>
      <Container maxWidth="lg">
        <AnimationFadeIn>
          <Grid container spacing={3} sx={{
            justifyContent: "center"
          }}>
            <Grid
              size={{
                xs: 12,
                sm: 10,
                lg: 6
              }}>
              <ImgCard>
                <CardContent sx={{ py: 5 }}>
                  <Box sx={{
                    textAlign: "center"
                  }}>
                    <Typography variant="h3" sx={{
                      fontWeight: 600
                    }}>
                      Haven&apos;t found an answer to your question?
                    </Typography>
                    <Typography variant="subtitle1" color="textSecondary" sx={{
                      mt: 1
                    }}>
                      Connect with us either on discord or email us
                    </Typography>
                  </Box>
                  <Stack
                    direction={{ xs: 'column', sm: 'row' }}
                    spacing={3}
                    sx={{
                      mt: 5,
                      justifyContent: "center",
                      mb: 3
                    }}>
                    <StyledButton
                      variant="contained"
                      color="primary"
                      href="https://discord.com/invite/XujgB8ww4n"
                    >
                      Ask on Discord
                    </StyledButton>
                    <StyledButton2
                      variant="outlined"
                      color="secondary"
                      href="https://adminmart.com/support"
                    >
                      Submit Ticket
                    </StyledButton2>
                  </Stack>
                </CardContent>
              </ImgCard>
            </Grid>
          </Grid>
        </AnimationFadeIn>
      </Container>
    </Box>)
  );
};

export default C2a;
