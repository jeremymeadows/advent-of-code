{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python314

    (python314.withPackages (ps: with ps; [
      requests
    ]))
  ];
}